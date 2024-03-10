import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import Controllers.AccountController;
import Domain.Employee;
import Domain.PersonComparator;
import Domain.Student;
import Domain.StudentGroup;
import Domain.Teacher;
import Services.StudentService;

public class App {
    public static void main(String[] args) throws Exception {

        Student s1 = new Student("Иван", 25);
        Student s2 = new Student("Игорь", 23);
        Student s3 = new Student("Иван", 22);
        Student s4 = new Student("Игорь",  23);
        Student s5 = new Student("Даша",  23);
        Student s6 = new Student("Лена",  23);

        List<Student> listStud = new ArrayList<Student>();
        listStud.add(s1);
        listStud.add(s2);
        listStud.add(s3);
        listStud.add(s4);
        listStud.add(s5);
        listStud.add(s6);
        

        StudentGroup group4580 = new StudentGroup(listStud, 4580);
        // System.out.println(group4580);

        // for(Student std : group4580)
        // {
        //     System.out.println(std);
        // }

        // System.out.println("=========================================================");

        // Collections.sort(group4580.getGroup());

        // for(Student std: group4580.getGroup())
        // {
        //     System.out.println(std);
        // }

        StudentService studServ = new StudentService();
        //AccountController contr = new AccountController();

        for(Student s : listStud)
        {
            studServ.create(s.getName(), s.getAge());
        }

        AccountController.print(studServ.getAll());

        studServ.sortByFIO();

        System.out.println("                             ");

        AccountController.print(studServ.getAll());


        Teacher t1 = new Teacher("Галина", 55, "Docent");
        Employee e1 = new Employee("Татьяна", 57, "Slesar");

        System.out.println(new PersonComparator<Student>().compare(s1, s3));

       // AccountController controller = new AccountController();
       // controller.paySalary(t1, 50000);
       // controller.paySalary(s1, 50000);

       AccountController.paySalary(t1, 50000);      
       //AccountController.paySalary(e1, 20000);
       
       System.out.println(AccountController.averageAge(listStud));


    }
}
