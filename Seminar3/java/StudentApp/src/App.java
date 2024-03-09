import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import Domain.Student;
import Domain.StudentGroup;

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
        

        StudentGroup group5830 = new StudentGroup(listStud, 5830);
        System.out.println(group5830);

        for(Student std : group5830)
        {
            System.out.println(std);
        }

        System.out.println("=========================================================");

        Collections.sort(group5830.getGroup());

        for(Student std: group5830.getGroup())
        {
            System.out.println(std);
        }

    }
}
