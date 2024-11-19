
import java.util.*;


class merge_arr
{
    public static void main(String[] args){
        int[] arr1 = {1,1,4,3,3};
        int[] arr2 = {2,2,5,7,3};
        LinkedHashSet<Integer> set = new LinkedHashSet<Integer>();

        int a1 = arr1.length;
        int a2 = arr2.length;

        int[] arr3 = new int[a1+a2];

        System.arraycopy(arr1, 0, arr3, 0, a1);
        System.arraycopy(arr2, 0, arr3, a1, a2);

        Arrays.sort(arr3);

        for(int var:arr3)
            set.add(var);
            // System.out.println(var);

        System.out.println(set);
    }
}