package Controllers;

import java.util.List;

import Domain.Person;
import Domain.Student;
import Domain.Teacher;

public class AccountController {

    public static <V extends Person> void print(List<V> group) {
        for(V s : group)
        {
            System.out.println(s);
        }
    }


    public static <T extends Teacher> void paySalary(T person, int salary) {
        System.out.println(person.getName() + " выплачено зарплата " + salary + "р. ");
    }

    //Загатовка для метода averageAge
    public static <T extends Person> double averageAge(List<T> persons)
    {
        return 0.0;
    }
}
