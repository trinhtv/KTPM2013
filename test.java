public class test
{

	static int giaipt ( int a, int b){
		if(a ==0) return 0;
			 return -b/a;
			//try{
				//return -b/a;
				//catch(){
				//return 0;
			//}
			//
		
	}

	static void test1(){

		 int ketqua = giaipt(1,1);
		if(ketqua == -1 )
		{
			System.out.println("dung");

		}
		else{
			System.out.println("sai");

		}
	}
	static void test2(){

		int ketqua = giaipt(10,-90);
			
		if(ketqua == 9 )
		{
			System.out.println("dung");

		}
		else{
			System.out.println("sai");

		}
	}
	static void test3(){

		int ketqua = giaipt(0,1);
			
		if(ketqua == 9 )
		{
			System.out.println("dung");

		}
		else{
			System.out.println("sai");

		}
	}
	public static void main (String [] args){
			int x = giaipt(0,1);

		test1();
		test2();
		test3();
	}

}