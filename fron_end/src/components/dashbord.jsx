import React, { useState, useEffect } from 'react';
import { Search, Upload, History, ChevronRight, Sparkles } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import FeedbackForm from './Feedback';

const mockUser = {
  name: localStorage.getItem("name"),
  lastLogin: "2024-01-18",
  cvLastUpdate: "2024-01-01"
};

const mockRecommendationHistory = [
  {
    id: 1,
    title: "Développeur Frontend React",
    company: "TechCorp",
    recommendedDate: "2024-01-15",
    status: "recommended",
    match: 95
  },
  {
    id: 2,
    title: "Lead Developer Full Stack",
    company: "StartupFlow",
    recommendedDate: "2024-01-10",
    status: "applied",
    match: 88
  },
  {
    id: 3,
    title: "DevOps Engineer",
    company: "CloudSys",
    recommendedDate: "2024-01-05",
    status: "viewed",
    match: 82
  }
];

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('history');
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const getGreeting = () => {
    const hour = new Date().getHours();
    if (hour < 12) return "Bonjour";
    if (hour < 18) return "Bon après-midi";
    return "Bonsoir";
  };

  const getStatusStyle = (status) => {
    const baseStyle = "font-medium text-sm px-3 py-1.5 rounded-full flex items-center gap-2 transition-all duration-500";
    switch (status) {
      case 'recommended':
        return `${baseStyle} bg-purple-100 text-purple-800 border border-purple-200 hover:bg-purple-200`;
      case 'applied':
        return `${baseStyle} bg-emerald-100 text-emerald-800 border border-emerald-200 hover:bg-emerald-200`;
      case 'viewed':
        return `${baseStyle} bg-sky-100 text-sky-800 border border-sky-200 hover:bg-sky-200`;
      default:
        return `${baseStyle} bg-gray-100 text-gray-800 border border-gray-200 hover:bg-gray-200`;
    }
  };
  const Navigate = useNavigate();
  const getStatusText = (status) => {
    const statusMap = {
      recommended: 'Recommandé',
      applied: 'Postulé',
      viewed: 'Consulté'
    };
    return statusMap[status] || status;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-purple-50 transition-all duration-1000">
      <div className="relative">
        {/* Animated background elements */}
        <div className="absolute inset-0 overflow-hidden">
          <div className="absolute -top-32 -left-32 w-64 h-64 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob" />
          <div className="absolute top-0 -right-32 w-64 h-64 bg-yellow-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-2000" />
          <div className="absolute -bottom-32 left-32 w-64 h-64 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-4000" />
        </div>

        <div className={`max-w-7xl mx-auto p-8 relative transition-opacity duration-1000 ${mounted ? 'opacity-100' : 'opacity-0'}`}>
          {/* Header Section */}
          <div className="bg-white/80 backdrop-blur-lg rounded-2xl shadow-lg mb-8 transform hover:scale-[1.02] transition-all duration-500">
            <div className="p-8">
              <div className="flex items-center justify-between">
                <div className="space-y-2">
                  <h1 className="text-4xl font-bold bg-gradient-to-r from-purple-600 via-purple-500 to-pink-500 bg-clip-text text-transparent animate-gradient">
                    {getGreeting()}, {mockUser.name} 
                    <span className="inline-block animate-wave ml-2">👋</span>
                  </h1>
                  <p className="text-gray-600 flex items-center gap-2 group">
                    <History className="w-4 h-4 group-hover:rotate-180 transition-transform duration-700" />
                    <span className="group-hover:text-purple-600 transition-colors duration-300">
                      CV mis à jour le {new Date(mockUser.cvLastUpdate).toLocaleDateString('fr-FR')}
                    </span>
                  </p>
                </div>
                <button className="group flex items-center gap-2 bg-gradient-to-r from-purple-600 to-purple-800 hover:from-purple-700 hover:to-purple-900 text-white px-6 py-3 rounded-lg transition-all duration-500 shadow-md hover:shadow-xl transform hover:-translate-y-1" onClick={() => Navigate("/upload")}>
                  <Upload className="w-5 h-5 group-hover:rotate-12 transition-transform duration-300" />
                  <span className="relative">
                    <span className="absolute -inset-1 rounded-lg bg-white/20 group-hover:blur animate-pulse"></span>
                    <span className="relative">Mettre à jour mon CV</span>
                  </span>
                </button>
              </div>
            </div>
          </div>

          {/* Tab Navigation */}
          <div className="flex gap-4 mb-8">
            <button 
              onClick={() => setActiveTab('history')}
              className={`group px-6 py-3 rounded-lg font-medium transition-all duration-500 shadow-sm relative overflow-hidden
                ${activeTab === 'history' 
                  ? 'bg-gradient-to-r from-purple-600 to-purple-800 text-white shadow-purple-200' 
                  : 'bg-white/80 backdrop-blur-sm text-purple-600 hover:bg-purple-50'}`}
            >
              <span className="relative z-10 flex items-center gap-2">
                <Sparkles className="w-5 h-5 group-hover:rotate-180 transition-transform duration-700" />
                Historique des recommandations
              </span>
            </button>
          </div>

          {/* Job History Cards */}
          <div className="grid gap-6">
            {mockRecommendationHistory.map((job, index) => (
              <div
                key={job.id}
                style={{ 
                  animationDelay: `${index * 150}ms`,
                  opacity: 0,
                  animation: 'slideIn 0.5s ease forwards'
                }}
                className="group bg-white/80 backdrop-blur-lg rounded-xl shadow-md hover:shadow-xl transition-all duration-500 p-6 hover:bg-white/90"
              >
                <div className="flex justify-between items-center">
                  <div className="space-y-2">
                    <div className="flex items-center gap-3">
                      <h3 className="text-xl font-semibold text-gray-900 group-hover:text-purple-600 transition-colors duration-300">
                        {job.title}
                      </h3>
                      <ChevronRight className="w-5 h-5 text-purple-400 group-hover:translate-x-2 transition-transform duration-500" />
                    </div>
                    <p className="text-gray-600 font-medium group-hover:text-purple-500 transition-colors duration-300">
                      {job.company}
                    </p>
                    <p className="text-gray-500 text-sm">
                      Recommandé le {new Date(job.recommendedDate).toLocaleDateString('fr-FR')}
                    </p>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className={getStatusStyle(job.status)}>
                      {getStatusText(job.status)}
                    </span>
                    <span className="bg-purple-100 text-purple-800 px-4 py-1.5 rounded-full text-sm font-medium border border-purple-200 group-hover:scale-105 transition-transform duration-300">
                      Match {job.match}%
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <style jsx>{`
        @keyframes blob {
          0% { transform: translate(0px, 0px) scale(1); }
          33% { transform: translate(30px, -50px) scale(1.1); }
          66% { transform: translate(-20px, 20px) scale(0.9); }
          100% { transform: translate(0px, 0px) scale(1); }
        }
        @keyframes slideIn {
          from { 
            opacity: 0;
            transform: translateY(20px);
          }
          to { 
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-blob {
          animation: blob 7s infinite;
        }
        .animation-delay-2000 {
          animation-delay: 2s;
        }
        .animation-delay-4000 {
          animation-delay: 4s;
        }
        .animate-wave {
          animation: wave 2.5s infinite;
        }
        @keyframes wave {
          0% { transform: rotate(0deg); }
          10% { transform: rotate(14deg); }
          20% { transform: rotate(-8deg); }
          30% { transform: rotate(14deg); }
          40% { transform: rotate(-4deg); }
          50% { transform: rotate(10deg); }
          60% { transform: rotate(0deg); }
          100% { transform: rotate(0deg); }
        }
        .animate-gradient {
          background-size: 200%;
          animation: gradient 8s linear infinite;
        }
        @keyframes gradient {
          0% { background-position: 0% 50%; }
          50% { background-position: 100% 50%; }
          100% { background-position: 0% 50%; }
        }
      `}</style>
      <FeedbackForm />
    </div>
  
  );
};

export default Dashboard;
