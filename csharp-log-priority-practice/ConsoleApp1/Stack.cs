public class Stack<T> {

    public List<T> stack;

    public Stack() {
        stack = new List<T>();
    }

    public void Push(T item) {
        stack.Add(item);
    }

    public T Pop() {
        if (Count() >= 1) {
            T item = stack[Count() - 1];
            stack.RemoveAt(Count() - 1);
            return item;
        }

        return default(T);
    }

    public int Count() {
        return stack.Count();
    }
    
}
