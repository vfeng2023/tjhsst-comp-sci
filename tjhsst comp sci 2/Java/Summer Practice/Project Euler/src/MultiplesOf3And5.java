/**
 * Problem: If we list all the natural numbers below 10 that are multiples of 3 or 5,
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */
public class MultiplesOf3And5 {
    public static void main(String[] args){
        //iterate through first 10000 numbers. if divisible by 3 or 5, add to sum.
        int sum=0;
        int limit = 1000;
        for(int i=1;i<limit;i++){
            if(i%3==0||i%5==0) sum += i;
        }
        //print sum
        System.out.println(sum);
    }
}
