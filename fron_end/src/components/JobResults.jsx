import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from "react-router-dom";
import { 
  Star, MapPin, Briefcase, Calendar, Link as LinkIcon, 
  GraduationCap, Laptop, Clipboard, Clock, UserCheck, 
  Sparkles 
} from 'lucide-react';

const MagicalJobResultsPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const [expandedJob, setExpandedJob] = useState(null);
  const [favorites, setFavorites] = useState([]);
  const [magicalEffects, setMagicalEffects] = useState({});

  const jobs = location.state?.jobs || [];

  const triggerMagicalEffect = (index) => {
    setMagicalEffects(prev => ({
      ...prev,
      [index]: {
        sparkle: true,
        timestamp: Date.now()
      }
    }));

    setTimeout(() => {
      setMagicalEffects(prev => {
        const updated = {...prev};
        delete updated[index];
        return updated;
      });
    }, 1500);
  };

  const toggleFavorite = (jobIndex) => {
    setFavorites(prev => 
      prev.includes(jobIndex) 
        ? prev.filter(index => index !== jobIndex)
        : [...prev, jobIndex]
    );
    triggerMagicalEffect(jobIndex);
  };

  const renderJobCard = (job, index) => {
    const isFavorite = favorites.includes(index);
    const isExpanded = expandedJob === index;
    const magicalEffect = magicalEffects[index];
    
    return (
      <div 
        key={index} 
        className={`
          relative group border-2 rounded-3xl p-6 transition-all duration-500 
          ${isFavorite ? 'border-purple-500 bg-purple-50/30' : 'border-gray-200'}
          transform hover:-translate-y-2 hover:shadow-2xl
        `}
      >
        {magicalEffect && (
          <div 
            className="absolute inset-0 pointer-events-none overflow-hidden"
            style={{
              animation: 'magical-sparkle 1.5s ease-out',
              animationFillMode: 'forwards'
            }}
          >
            <div className="absolute top-0 left-0 w-full h-full bg-purple-100/50 opacity-0 animate-magical-reveal"></div>
            <Sparkles 
              className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-purple-500" 
              size={100} 
              strokeWidth={1.5}
            />
          </div>
        )}

        <div className="relative z-10">
          <div className="absolute top-0 right-0 flex space-x-3">
            <button 
              onClick={() => toggleFavorite(index)}
              className="hover:scale-125 transition-transform"
            >
              <Star 
                color={isFavorite ? '#8B4FFF' : 'gray'} 
                fill={isFavorite ? '#8B4FFF' : 'transparent'}
                className={isFavorite ? 'animate-pulse' : ''}
              />
            </button>
          </div>

          <div className="space-y-4">
            <h3 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-blue-600">
              {job.job_title}
            </h3>
            
            <div className="grid grid-cols-2 gap-4">
              <div className="flex items-center space-x-3">
                <Briefcase className="text-blue-500" />
                <span>{job.company}</span>
              </div>
              <div className="flex items-center space-x-3">
                <MapPin className="text-green-500" />
                <span>{job.location}</span>
              </div>
            </div>

            <div className="bg-gray-100/50 rounded-xl p-4 border border-gray-200/50">
              <div className="grid grid-cols-2 gap-3 mb-3">
                <div className="flex items-center space-x-2">
                  <Calendar className="text-red-500" />
                  <span>{job.publication_date}</span>
                </div>
                <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-center">
                  {job.contract}
                </span>
              </div>

              {expandedJob === index && (
                <div className="space-y-3">
                  <div className="grid md:grid-cols-2 gap-3">
                    <div className="flex items-center space-x-2">
                      <UserCheck className="text-purple-500" />
                      <span><strong>Expérience:</strong> {job.experience}</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <GraduationCap className="text-teal-500" />
                      <span><strong>Études:</strong> {job.education}</span>
                    </div>
                  </div>

                  <div>
                    <strong>Compétences:</strong>
                    <div className="flex flex-wrap gap-2 mt-2">
                      {job.skills.map((skill, idx) => (
                        <span 
                          key={idx} 
                          className="bg-purple-200/50 text-purple-800 px-2 py-1 rounded-full text-xs"
                        >
                          {skill}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              )}
            </div>

            <div className="flex justify-between items-center mt-4">
              <button 
                onClick={() => setExpandedJob(isExpanded ? null : index)}
                className="flex items-center space-x-2 text-purple-600 hover:text-purple-800"
              >
              
                <span>{isExpanded ? 'Réduire' : 'Détails '}</span>
              </button>

              <a 
                href={job.link} 
                target="_blank" 
                rel="noopener noreferrer"
                className="
                  bg-gradient-to-r from-purple-500 to-blue-500 
                  text-white px-4 py-2 rounded-full 
                  hover:from-purple-600 hover:to-blue-600
                  transition-all duration-300
                "
              >
                Postuler
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-blue-50 p-10">
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-10">
          <h1 className="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-blue-600">
            ✨ Carrières 
          </h1>
          <button 
            onClick={() => navigate("/upload")}
            className="
              px-5 py-2.5 
              bg-gradient-to-r from-purple-500 to-blue-500
              text-white rounded-full 
              hover:from-purple-600 hover:to-blue-600
              transition-all duration-300
            "
          >
            Retour
          </button>
        </div>

        {jobs.length === 0 ? (
          <div className="text-center py-20 bg-white/50 rounded-3xl shadow-xl">
            <p className="text-3xl text-gray-500">
              🔮 Aucune offre magique trouvée
            </p>
          </div>
        ) : (
          <div className="space-y-6">
            {jobs.map(renderJobCard)}
          </div>
        )}
      </div>

      <style jsx global>{`
        @keyframes magical-sparkle {
          0% { opacity: 0; transform: scale(0.5); }
          50% { opacity: 1; transform: scale(1.2); }
          100% { opacity: 0; transform: scale(1.5); }
        }
        .animate-magical-reveal {
          animation: magical-reveal 1.5s ease-out;
        }
        @keyframes magical-reveal {
          0% { opacity: 0; }
          50% { opacity: 0.5; }
          100% { opacity: 0; }
        }
      `}</style>
    </div>
  );
};

export default MagicalJobResultsPage;