const express = require("express");
const path = require("path");

const db = require("./database");

const app = express();
app.use(express.static("public"));

app.get("/db/", (req, res) => {
  // res.send("hello");
  tb_name = req.query.s;
  if (!tb_name.match(/(hole|room)[A-C1-2]_Day[1-3]_[1-5]/g)) {
    res.send([{ tweet_str_id: "1369848266385330183" }]);
    return;
  }
  db.pool.connect((err, client) => {
    if (err) {
      console.log(err);
      res.send(err);
    } else {
      // client.query("SELECT name FROM test", (err, result) => {
      (async () => {
        await client.query(
          `SELECT * FROM ${tb_name} ORDER BY id desc limit 10`,
          (err, result) => {
            if (err) {
              console.log(err);
              res.send([{ tweet_str_id: "1369848266385330183" }]);
            } else {
              // console.log(result.rows);
              // res.send(result.rows.slice(0, 10));
              if (result == undefined) {
                res.send([{ tweet_str_id: "1369848266385330183" }]);
              } else {
                res.send(result.rows);
                console.log(result.rows);
              }
            }
          }
        );
        assert(client.release === release);
      })();
    }
  });
});

app.get("/test/", (req, res) => {
  tb_name = req.query.s;
  res.send(tb_name);
});

const port = process.env.PORT || 5000;
app.listen(port);

console.log("server started " + port);
