
import java.util.HashMap ; import java.util.HashSet ; import java.util.Scanner ; public class Main { public static void main ( String [ ] args ) { Scanner sc = new Scanner ( System.in ) ; int n = sc.nextInt ( ) ; int m = sc.nextInt ( ) ; String arrs [ ] = new String [ n ] ; for ( int i = 0 ; i < n ; i ++ ) { arrs [ i ] = sc.next ( ) ; } int [ ] length = new int [ n ] ; int index = 0 ; int returnDex = 0 ; for ( String tmp : arrs ) { int dexG = tmp.indexOf ( "G" ) ; int dexS = tmp.indexOf ( "S" ) ; if ( dexG > dexS ) { returnDex = - 1 ; } length [ index ++ ] = dexS - dexG ; } HashSet set = new HashSet < Integer > ( ) ; for ( int len : length ) { set.add ( len ) ; } if ( returnDex == - 1 ) { System.out.println ( returnDex ) ; } else { System.out.println ( set.size ( ) ) ; } } }

