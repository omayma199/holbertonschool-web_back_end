function getStudentsByLocation(students, city) {
  // Use the filter function to get students located in the specified city
  const studentsInCity = students.filter(student => student.location === city);
  return studentsInCity;
}
