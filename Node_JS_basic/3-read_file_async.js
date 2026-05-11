// 3-read_file_async.js

const fs = require('fs');

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

      // Remove header
      const students = lines.slice(1).filter((line) => line.trim() !== '');

      console.log(`Number of students: ${students.length}`);

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
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
