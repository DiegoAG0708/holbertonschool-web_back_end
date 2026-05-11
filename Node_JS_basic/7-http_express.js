// 7-http_express.js

const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;
const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = lines.slice(1).filter((line) => line.trim() !== '');
      let output = `Number of students: ${students.length}\n`;

      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[3];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      });

      for (const [field, list] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');
  countStudents(database)
    .then((report) => {
      res.end(report);
    })
    .catch(() => {
      res.end('Cannot load the database');
    });
});

app.listen(port);

module.exports = app;
