import "./App.css";
import Home from "./Pages/Home";
import SearchResult from "./Pages/SearchResult";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Pages/Login";
import Register from "./Pages/Register";

function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    
                    <Route exact path="/home" element={<Home />} />
                    <Route exact path="/" element={<Login />} />
                    <Route exact path="/login" element={<Login />} />
                    <Route exact path="/register" element={<Register />} />
                    <Route
                        exact
                        path="/search/:id"
                        element={<SearchResult />}
                    />
                </Routes>
            </Router>
        </div>
    );
}

export default App;
