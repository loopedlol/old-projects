public class Queue<T> {

    public List<T> queue;

    public Queue() {
        queue = new List<T>();
    }

    public void Insert(T item) {
        queue.Add(item);
    }

    public T Pop() {
        if (Count() >= 1) {
            T item = queue[0];
            queue.RemoveAt(0);
            return item;
        }

        return default(T);
    }

    public int Count() {
        return queue.Count();
    }
    
}
