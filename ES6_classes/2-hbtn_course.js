class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this._validateString(name, 'name');
    this._length = this._validateNumber(length, 'length');
    this._students = this._validateStudents(students, 'students');
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this._validateString(newName, 'name');
  }

  // Getter and setter for length
  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = this._validateNumber(newLength, 'length');
  }

  // Getter and setter for students
  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = this._validateStudents(newStudents, 'students');
  }

  // Helper method to validate a string attribute
  _validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attributeName} must be a string`);
    }
    return value;
  }

  // Helper method to validate a number attribute
  _validateNumber(value, attributeName) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new TypeError(`${attributeName} must be a valid number`);
    }
    return value;
  }

  // Helper method to validate an array of strings for students
  _validateStudents(value, attributeName) {
    if (!Array.isArray(value) || !value.every((item) => typeof item === 'string')) {
      throw new TypeError(`${attributeName} must be an array of strings`);
    }
    return value;
  }
}

// Example usage:
const course = new HolbertonCourse('Web Development', 12, ['Alice', 'Bob', 'Charlie']);
console.log(course.name); // Output: Web Development
console.log(course.length); // Output: 12
console.log(course.students); // Output: ['Alice', 'Bob', 'Charlie']

course.name = 'Data Science'; // Setting a new name
console.log(course.name); // Output: Data Science
