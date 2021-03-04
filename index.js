const express = require("express");
const path = require("path");

const db = require("./database");

const app = express();
app.use(express.static("public"));

app.get("/db/", (req, res) => {
  // res.send("hello");
  db.pool.connect((err, client) => {
    if (err) {
      console.log(err);
      res.send(err);
    } else {
      client.query("SELECT name FROM test", (err, result) => {
        console.log(result.rows);
        res.send(result.rows);
      });
    }
  });
});

const port = process.env.PORT || 5000;
app.listen(port);

console.log("server started " + port);
