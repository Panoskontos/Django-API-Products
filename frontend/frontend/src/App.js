import axios from "axios";
import React from "react";

// Api url
const baseURL = "http://127.0.0.1:8000/api/movies/";

function App() {

  // fetch data 
  const [movies, setmovies] = React.useState(null);

  React.useEffect(() => {

    axios.get(baseURL).then((response) => {
      console.log(response.data)
      setmovies(response.data);
    });
  }, []);


  // return html

  if (!movies){
    return null
  } else {
    return (

      <div>
    {movies.map((movie, index) => {
      return (
        <div>
          <h2>{movie.name} - {movie.genre} - {movie.starring}</h2>
        </div>
      )
    })}
    </div>
    )
  }

 
}

export default App;
