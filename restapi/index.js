const express = require( 'express' );
var mysql = require('mysql');
const app = express()
const PORT = 8080
const maxID = 4000

app.use( express.json() )

var db = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
});

app.listen(PORT, () => {
    console.log(`server started at http://localhost:${PORT}`)
})

app.get('/info/:sn', (req, res) =>{
    const { sn } = req.params;
    const wildcard = `${sn}%`;
    var sql = "select ID, TransID from bjt where TransID like ?";
    db.query(sql, [wildcard], function (err, result) {
        if (err){
            console.error(err)
            res.status(500).send({message: err})
        }
        else if(result.length==0){
            res.status(404).send({message: `No transistor by name ${sn} in database.`})
        }
        else if(result.length==1){
            sql = "select * from bjt where ID = " + mysql.escape(result[0].ID);
            db.query(sql, function (err, result){
                res.status(200).send({
                    message: `Information on Transistor ${result[0].TransID}`,
                    result: result
                });
            })
        }
        else{
            res.status(200).send({
                message: 'Too many similar names, new get request to /info/id/{ID of Specific Transistor}',
                result: result
            });
        }
        
    });
});

app.get('/info/id/:id', (req, res) =>{
    const { id } = req.params;
    if (isNaN(Number(id))) {
        return res.status(400).send({ message: 'Invalid ID. Please provide a numeric value.' });
    }
    if(id>maxID || id <= 0){
        return res.status(404).send({message: `ID ${id} is out of bounds.`})
    }
    var sql = "select * from bjt where ID = " + mysql.escape(id);
    db.query(sql, function (err, result) {
        if(err){
            console.error(err);
            res.status(500).send({message: err})
        }
        res.status(200).send({
            message: `Information on Transistor ${result[0].TransID}`,
            result: result
        });
    })
});

app.get('/equal/:sn', (req, res) => {
    const { sn } = req.params;
    const wildcard = `${sn}%`
    var sql = "select ID, TransID from bjt where TransID like ?";
    db.query(sql, [wildcard], function (err, result) {
        if (err){
            console.error(err)
            return res.status(500).send({message: err})
        }
        if(result.length==0){
            res.status(404).send({message: `No transistor by name ${sn} in database.`})
        }
        else if(result.length==1){
            var compare = [result[0].Material, result[0].Structure, result[0].Pc, result[0].Vcb, result[0].Vce, result[0].Ic, result[0].Temp, result[0].Ft, result[0].Cc, result[0].Hfe];
            sql = "select * from bjt where Material = ? and Structure = ? and Pc >= ? and Vcb >= ? and Vce >= ? and Ic >= ? and Temp >= ? and Ft >= ? and Cc <= ? and Hfe >= ?"
            db.query(sql, compare, function (err, resultin){
                if(err){
                    console.error(err);
                    return res.status(500).send({message: err})
                }
                if(resultin.length>1){
                    resultin = resultin.filter(item => item.ID != id)
                    res.status(200).send({
                        message: `Equivalent Transistor(s) for ${result[0].TransID}`,
                        result: resultin
                    });
                }
                else{
                    res.status(200).send({message: `No equivalent transistor for ${result[0].TransID}`})
                }
            })
        }
        else{
            res.status(200).send({
                message: 'More than one similar name, send new get request to /equal/id/{ID of Specific Transistor}',
                result: result
            });
        }
        
    });
});

app.get('/equal/id/:id', (req, res) =>{
    const { id } = req.params;
    if (isNaN(Number(id))) {
        return res.status(400).send({ message: 'Invalid ID. Please provide a numeric value.' });
    }
    if(id>maxID || id <= 0){
        return res.status(404).send({message: `ID ${id} is out of bounds.`})
    }   
    var sql = "select * from bjt where ID = " + mysql.escape(id);
    db.query(sql, function (err, result) {
        if(err){
            console.error(err);
            return res.status(500).send({message: err})
        }
        
        var compare = [result[0].Material, result[0].Structure, result[0].Pc, result[0].Vcb, result[0].Vce, result[0].Ic, result[0].Temp, result[0].Ft, result[0].Cc, result[0].Hfe];
        sql = "select * from bjt where Material = ? and Structure = ? and Pc >= ? and Vcb >= ? and Vce >= ? and Ic >= ? and Temp >= ? and Ft >= ? and Cc <= ? and Hfe >= ?"
        db.query(sql, compare, function (err, resultin){
            if(err){
                console.error(err);
                return res.status(500).send({message: err})
            }
            if(resultin.length>1){
                resultin = resultin.filter(item => item.ID != id)
                res.status(200).send({
                    message: `Equivalent Transistor(s) for ${result[0].TransID}`,
                    result: resultin
                });
            }
            else{
                res.status(200).send({message: `No equivalent transistor for ${result[0].TransID}`})
            }
        })

    })
});
