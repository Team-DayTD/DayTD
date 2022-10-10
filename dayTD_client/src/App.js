import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Navbar from './components/navbar';
import Main from './Pages/MainPage/Main';
import Like from './Pages/LikePage/Like';
import MyPage from './Pages/MyPage';
import SignUp from './Pages/SignUp';
import "./style/main.scss";
import Footer from './components/footer';

function App() {
  return (
    <div className="app">
      <BrowserRouter>
        <Navbar/>
        <Routes>
          <Route path="/" element={<Main reset='best'/>}></Route>
          <Route path="/Main" element={<Main reset='best'/>}></Route>
          <Route path="/Like" element={<Like/>}></Route>
          <Route path="/MyPage" element={<MyPage/>}></Route>
          <Route path="/SignUp" element={<SignUp/>}></Route>
        </Routes>
        <Footer/>
      </BrowserRouter>
    </div>
  );
}

export default App;
