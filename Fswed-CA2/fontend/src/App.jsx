import { useState } from "react";
import './App.css';

function App() {
  const [name, setauthor] = useState("");
  const [title, setTitle] = useState("");
  const [submission, setSubmission] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault()
    setSubmission([...submission, {title,author}])
    setauthor("")
    setTitle("")
  }

  return (
    <>
      <div className="app">
        <from onSubmit="submit">
          <h1>Book collection</h1>
          <input
            type="text"
            placeholder="author of the book"
            value={author}
            onChange={(e) => setauthor(e.target.value)}
            required
          />
          
          <input
            type="text"
            placeholder="Title of the book"
            value={title}
            onChange={(e) => setitle(e.target.value)}
            required
          />
          <button type="submit">Submit</button>

        </from>
        

      </div>
      <div>
        <h2>Add new books</h2>
          <li>
            {submission.map((book,index) => {
              <ul>
                {book.author}  - {book.title}
              </ul>
            ))}

          </li>
      </div>
    </>
  );
}