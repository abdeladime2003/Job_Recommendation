import React, { useState, useEffect } from 'react';
import { Menu, X, ChevronDown, Upload, Search, Book } from 'lucide-react';
const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [scrolled, setScrolled] = useState(false);
  
    useEffect(() => {
      const handleScroll = () => {
        setScrolled(window.scrollY > 20);
      };
      window.addEventListener('scroll', handleScroll);
      return () => window.removeEventListener('scroll', handleScroll);
    }, []);
  
    return (
      <nav className={`fixed w-full z-50 transition-all duration-300 ${
        scrolled ? 'bg-white text-blue-600 shadow-lg' : 'bg-transparent text-white'
      }`}>
        <div className="max-w-7xl mx-auto flex justify-between items-center px-4 py-4">
          <h1 className="text-2xl font-bold hover:scale-105 transition duration-300">
            JobFinder
          </h1>
  
          <button
            className="md:hidden hover:rotate-180 transition-transform duration-300"
            onClick={() => setIsOpen(!isOpen)}
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
  
          <ul className={`${
            isOpen ? 'translate-x-0' : 'translate-x-full'
          } md:translate-x-0 fixed md:relative top-16 md:top-0 right-0 h-screen md:h-auto w-64 md:w-auto 
          bg-white md:bg-transparent md:flex space-y-4 md:space-y-0 md:space-x-8 p-6 md:p-0
          transform transition-transform duration-300 ease-in-out shadow-lg md:shadow-none`}>
            {['Accueil', 'Fonctionnalités', 'Contact'].map((item, index) => (
              <li key={index} className="relative group">
                <a href={`#${item.toLowerCase()}`} 
                   className="block py-2 group-hover:text-blue-400 transition-colors duration-300">
                  {item}
                  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-blue-400 group-hover:w-full transition-all duration-300"></span>
                </a>
              </li>
            ))}
          </ul>
        </div>
      </nav>
    );
  };
export default Navbar;
