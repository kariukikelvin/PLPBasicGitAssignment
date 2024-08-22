class teacher{
  String name;
  int age;
  String subject;

  teacher(this.name, this.age, this.subject);

  void displayInfo(){
    print('Teacher Information:');
    print('Name: $name');
    print('Age: $age');
    print('Gradelevel:$subject');
  }

}


class student{
  String name;
  int age;
  String gradeLevel;

  student(this.name, this.age, this.gradeLevel);

  void displayInfo(){
    print('Student Information:');
    print('Name: $name');
    print('Age: $age');
    print('Gradelevel:$gradeLevel');
    

  }

}

void main(){
  student Student = student('Alex', 20, '10th gradeLevel');

  teacher Teacher = teacher('Mr.Mark', 50, 'Maths');

  Student.displayInfo();

  
  Teacher.displayInfo();

}

