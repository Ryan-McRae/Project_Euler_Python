import random

#HEADS = 0
#TAILS = 1
"""
BREAK WHEN 00 OR 01
ALICE = 00
BOB = 01
"""
toss = ["H","T"]

for i in range(0,3):

    c1 = 9
    c2 = 9
    an = ""
    bn = ""

#ALICE
    while 1 == 1:
    
        q1 = random.randrange(0,2)

        c1 = c2
        c2 = q1
        an += toss[q1]

        if((c1 == 0) and (c2 == 0)): #ALICE
            #print("ALICE - " + an)
            break 

    c1 = 9
    c2 = 9
#BOB
    while 1 == 1:
    
        q1 = random.randrange(0,2)

        c1 = c2
        c2 = q1
        bn += toss[q1]

        if((c1 == 0) and (c2 == 1)): #BOB
            #print("BOB - " + bn)
            break

    if (len(an) < len(bn)):
        print("Alice:" + an + " Bob:" + bn + " Alice has fewer")
    else:
        print("Alice:" + an + " Bob:" + bn)   
    print("\n")






"""
public class TUT1{
  public static void main(String args[]){

    int n = Integer.parseInt(args[0]);
    int alice = 0;


    /*HEADS == 0    TAILS == 1
    BREAKS WHEN 00 OR 01 [HH OR HT]
    ALICE = 00
    BOB = 01
*/
    char[] toss;
    toss = new char[2];
    toss[0] = 'H';
    toss[1] = 'T';
    int q1;

    for (int i = 0; i < n; i++){

      //CONSIDER THESE LOCAL
      int c1 = 9;
      int c2 = 9;
      //CONSIDER THESE GLOBAL
      String an = "";
      String bn = "";

/////////////////////////////////////////////////////
//ALICE
      while (1 == 1){

        int q = (int) (Math.random()*10);
        if ((0 <= q) && (q <= 4)){
          q1 = 0;
        }
        else{
          q1 = 1;
        }

        c1 = c2;
        c2 = q1;
        an += toss[q1];

        if((c1 == 0) && (c2 == 0)){
          break;
        }
      }

/////////////////////////////////////////////////////
      //LOCAL VARIBALES REFRESHED
      c1 = 9;
      c2 = 9;
//BOB
      while (1 == 1){

        int q = (int) (Math.random()*10);
        if ((0 <= q) && (q <= 4)){
          q1 = 0;
        }
        else{
          q1 = 1;
        }

        c1 = c2;
        c2 = q1;
        bn += toss[q1];

        if((c1 == 0) && (c2 == 1)){
          break;
        }
      }
/////////////////////////////////////////////////////

      if((an.length())<(bn.length())){
        alice+=1;
        //System.out.println("Alice:" + an + " Bob:" + bn + " Alice has fewer");
      }
      //else{
        //System.out.println("Alice:" + an + " Bob:" + bn);  
      //}
    }
    System.out.println(((double)(alice)/(double)(n)));
  }
}
"""