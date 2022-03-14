import './App.css';
import React,{useEffect,useState} from 'react'
function App() {
  const [users,setUser]=useState([])
  useEffect(()=>{
    fetch("http://127.0.0.1:8000/").then((result)=>{
      result.json().then((resp)=>{
        setUser(resp)
      })
    })
  },[])
  console.warn(users)
  return (
    
    <div>    
      <h1 className="head__text">News App 👋</h1>
      {
        <div className="all__news">
          {
            users && users.map((item, i) => {

              return <div className="news">
                <img src={item.urlToImage} alt="new" width="390"/>
                <h1 className="news__title">{item.title}</h1>
                <p className="news__desc">{item.description}</p>
                <span className="news__author">{item.author}</span> <br />
                <span className="news__published">{item.publishedAt}</span><br /><br />
                <a className="news__readmore" href={item.url}>Read more</a>
                  
              </div>

              
            })
          }
        </div>

      }
    </div>

    
  );
}
export default App;