import java.util.Scanner;
class LoanCalculate{
	double princi,rate,fee;
	int tenure;
	LoanCalculate(double princi,double rate,int tenure,double fee){
		this.princi=princi;
		this.rate=rate;
		this.tenure=(tenure>0)?tenure:1;
		this.fee=(fee>=0)?fee:0;
	}
	double CalculateLoan(){
		return princi+(princi*rate/100);
	}
	double CalculateLoan(int tenure){
		return princi*Math.pow(1+rate/100,tenure);
	}
	double CalculateLoan(int tenure,double fee){
		return CalculateLoan(tenure)+fee;
	} 
	public static void main(String[] args){
		Scanner scanner=new Scanner(System.in);
		
		System.out.print("Principal:");
		double p=scanner.nextDouble();
		System.out.print("Rate:");
		double  r=scanner.nextDouble();
		System.out.print("Tenure:");
		int t=scanner.nextInt();
		System.out.print("Fee:");
		double  f=scanner.nextDouble();
		
		LoanCalculate ploan= new LoanCalculate(p,r,1,0);
		LoanCalculate hloan= new LoanCalculate(p,r,t,0);
		LoanCalculate cloan= new LoanCalculate(p,r,t,f);
		
		System.out.println("Personal Loan:"+ ploan.CalculateLoan());
		System.out.println("Home Loan:"+ hloan.CalculateLoan(t));
		System.out.println("Car Loan:"+ cloan.CalculateLoan(t,f));
	}
}