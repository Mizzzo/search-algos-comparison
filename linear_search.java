import java.util.ArrayList;

public class linear_search {
    public static Boolean search(ArrayList<Integer> input_list, int target){
        for(int curr:input_list){
            if (curr == target){
                return true;
            }
        }


        return false;
    }

    public static ArrayList<Integer> create_d(int n){
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i<n;i++){
            list.add(i);
        }

        return list;
    }
    public static void main(String[]args){
        int n = 10000000;
        ArrayList<Integer> ma_list = create_d(n);

        boolean res = search(ma_list, n - 1);
        System.out.println(Boolean.toString(res));
    }
}
