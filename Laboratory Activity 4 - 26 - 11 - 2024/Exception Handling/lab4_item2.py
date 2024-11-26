def main():
    try:
        size = int(input("Enter the size of the array: "))
        if size <= 0:
            raise ValueError("Size must be positive.")

        arr = [0.0] * size
        
        print("Enter the elements of the array:")
        for i in range(size):
            arr[i] = float(input())
            
        index = int(input("Enter the index of the element to print: "))
        
        print(f"Element at index {index}: {arr[index]:.2f}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except IndexError:
        print(f"Index {index} is invalid.")

if __name__ == "__main__":
    main()