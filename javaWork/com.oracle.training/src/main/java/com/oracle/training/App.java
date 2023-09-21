package com.oracle.training;

import com.oracle.training.data.*;
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
        Oracle Employee1 = new Oracle(10, 10, "Tanaka", "Tech");
        Oracle2 Employee2 = new Oracle2(20, 20, "Sato", "Apps");
        // Oracle3 Employee3 = new Oracle3(30, 30, "Suzuki", "Sales");
        System.out.println(Employee1.getEmployeeNum());
        System.out.println(Employee2.getEmployeeNum());
        // System.out.println(Employee3.getEmployeeNum());
    }
}
