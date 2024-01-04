function getListStudentIds(students) {
    // Check if the input is an array
    if (!Array.isArray(students)) {
      return [];
    }

    // Use the map function to extract ids from the array of objects
    const ids = students.map(student => student.id);
    return ids;
  }
