
public class BinarySearch

int BinarySearch(int [] arr, int key, int low, int high){
	if(false ==isSorted(arr))
	return    

	if(key<arr[0] || key > arr[arr.length-1])
	return // If key is out of range

	int mid=0
	int res=-1

	while(low<=high){
	mid=(low+high)/2

	if(arr [mid]==key){
	res=mid
	break;
	} else if(arr[mid] <key){
	;low=mid+1
	}else {
	high=mid-1
	}
	}
	return res
	}
