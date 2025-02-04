import React from 'react';
// import private route
import PrivateRoute from './components/PrivateRoute';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import HomePage from './components/Homepage';
import Signup from './components/Signup';
import NotFound  from './components/NotFound';
import Signin from './components/Signin';
import ImageClassifier from './components/dashbord';
import CVUpload from './components/CvUpload';
import VerifyEmail from './components/verifyemail';
import JobResults from './components/JobResults';
import Dashboard from './components/dashbord';
function App() {
  return ( 
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="signup" element={<Signup />}/>
        <Route path='signin' element = {<Signin/>}/> 
        <Route path="upload" element={<PrivateRoute Component={CVUpload}/>}/>
        <Route path="/verify-email/:token" component={VerifyEmail} />
        <Route path="jobs" element={<PrivateRoute Component={JobResults}/>}/>
        <Route path="dashboard" element={<PrivateRoute Component={Dashboard}/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </BrowserRouter>
  );
}
export default App;
