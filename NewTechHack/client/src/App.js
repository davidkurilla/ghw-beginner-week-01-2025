import logo from './logo.svg';
import { useState, useEffect } from 'react';

function App() {

  const [todoList, setTodoList] = useState([]);
  const [newTodo, setNewTodo] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);

  const base_url = "http://localhost:5000/todos";

  useEffect(() => {
    fetch(base_url).then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      setTodoList(data);
      setIsLoaded(true);
    })
    .catch((err) => {
      setError(err);
      setIsLoaded(true);
    })
  }, []);

  const addTodo = () => {
    fetch(base_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: newTodo })
    }).then((response) => {
      if (!response.ok) {
        throw new Error("Failed to add todo");
      }
      return response.json();
    })
    .then((newItem) => {
      setTodoList([...todoList, newItem]);
      setNewTodo("");
    })
    .catch((err) => setError(err));
  };

  const deleteTodo = (id) => {
    fetch(`${base_url}/${id}`, {method: "DELETE",}).then((response) => {
      if (!response.ok) {
        throw new Error("Failed to delete todo!");
      }
      setTodoList(todoList.filter((todo => todo.id !== id)));
    }).catch((err) => {
      setError(err);
    })
  };

  if (error) {
    return <div>Error: {error.message}</div>
  }

  if (!isLoaded) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <h1>My Todo List</h1>
      <div>
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Add a new todo"
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <ul>
        {todoList.map((todo) => (
          <li key={todo.id}>
            {todo.message}
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
