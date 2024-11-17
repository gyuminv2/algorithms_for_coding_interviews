def bubble_sort(list, n){
  for i in range(n-1, 0, -1):
    for j in range(0, i, 1):
      if list[j] < list[j+1]:
        tmp = list[j];
        list[j] = list[j+1];
        list[j+1] = tmp;
      }
    }
  }
}
