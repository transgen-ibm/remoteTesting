
import java.util.ArrayList ; import java.util.Scanner ; import java.lang.Math ; public class Main { static final int INF = ( int ) 1e9 + 5 ; public static void main ( String [ ] args ) { Scanner sc = new Scanner ( System.in ) ; int n ; n = sc.nextInt ( ) ; ArrayList < Integer > a = new ArrayList < > ( ) ; ArrayList < Integer > b = new ArrayList < > ( ) ; int left = INF, right = 0 ; for ( int i = 0 ; i < n ; i ++ ) { a.add ( sc.nextInt ( ) ) ; b.add ( sc.nextInt ( ) ) ; left = Math.min ( left, a.get ( i ) ) ; right = Math.max ( right, b.get ( i ) ) ; } for ( int i = 0 ; i < n ; i ++ ) { if ( left == a.get ( i ) && right == b.get ( i ) ) { System.out.println ( ++ i ) ; return ; } } System.out.println ( - 1 ) ; } }

