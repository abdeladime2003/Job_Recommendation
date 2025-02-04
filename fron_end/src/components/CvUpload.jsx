import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Upload, X, FileText, Check, AlertCircle, Sparkles, Star } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
const CVUpload = () => {
  const [dragActive, setDragActive] = useState(false);
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState(null);
  const [mounted, setMounted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigate = useNavigate();
  useEffect(() => {
    setMounted(true);
    return () => setMounted(false);
  }, []);

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(e.type === 'dragenter' || e.type === 'dragover');
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    handleFile(e.dataTransfer.files[0]);
  };

  const handleChange = (e) => {
    handleFile(e.target.files[0]);
  };

  const handleFile = (uploadedFile) => {
    if (!uploadedFile) return;
    
    if (uploadedFile.type === 'application/pdf' && uploadedFile.size <= 5 * 1024 * 1024) {
      setFile(uploadedFile);
      setUploadStatus('ready');
    } else {
      setUploadStatus('error');
      setFile(null);
    }
  };

  const removeFile = () => {
    setFile(null);
    setUploadStatus(null);
  };

  const uploadFile = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);
    console.log('Uploading:', file);
    try {
      setUploadStatus('uploading');
      
      const response = await axios.post('http://localhost:8000/cvs/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      });
      console.log('Upload response:', response.data);
      setUploadStatus('success');
      navigate('/jobs', { state: { jobs: response.data.recommendations } });
    } catch (error) {
      console.error('Erreur d\'upload:', error);
      setUploadStatus('error');
    }
  };

  useEffect(() => {
    if (file && uploadStatus === 'ready') {
      uploadFile();
    }
  }, [file, uploadStatus]);

  const features = [
    {
      icon: <Star className="w-6 h-6" />,
      title: "Format PDF",
      desc: "Pour une mise en page parfaite"
    },
    {
      icon: <Upload className="w-6 h-6" />,
      title: "5 MB max",
      desc: "Taille optimale recommandée"
    },
    {
      icon: <FileText className="w-6 h-6" />,
      title: "CV optimal",
      desc: "Clair, concis et impactant"
    }
  ];

  return (
    <div className="relative min-h-screen overflow-hidden bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50">
      {/* Animated background */}
      <div className="absolute inset-0 pointer-events-none">
        <div className="absolute top-0 -left-10 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob" />
        <div className="absolute top-0 -right-10 w-72 h-72 bg-yellow-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-2000" />
        <div className="absolute bottom-0 left-20 w-72 h-72 bg-pink-300 rounded-full mix-blend-multiply filter blur-xl opacity-30 animate-blob animation-delay-4000" />
      </div>

      <div className={`relative max-w-4xl mx-auto p-8 transition-all duration-1000 ${mounted ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'}`}>
        {/* Header */}
        <div className="text-center mb-12 relative">
          <div className="absolute -top-10 left-1/2 transform -translate-x-1/2">
            <div className="relative">
              <Star className="w-8 h-8 text-yellow-400 animate-spin-slow" />
              <Sparkles className="absolute top-0 right-0 w-4 h-4 text-yellow-400 animate-pulse" />
            </div>
          </div>
          <h1 className="text-5xl font-bold mb-6 bg-gradient-to-r from-purple-600 via-pink-500 to-indigo-600 bg-clip-text text-transparent animate-gradient">
            Propulsez votre carrière
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
            Déposez votre CV et laissez la magie opérer ✨
          </p>
        </div>

        {/* Upload Area */}
        <div
          className={`relative rounded-3xl transition-all duration-500 transform 
            ${dragActive ? 'scale-105 bg-purple-50/90 border-purple-400' : 'scale-100 bg-white/80 border-gray-200'} 
            ${uploadStatus === 'success' ? 'border-green-400' : ''} 
            backdrop-blur-xl border-2 border-dashed p-12 shadow-2xl hover:shadow-purple-200/50`}
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
        >
          <input
            type="file"
            accept=".pdf"
            onChange={handleChange}
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
          />

          <div className="flex flex-col items-center justify-center gap-6">
            {!file && (
              <>
                <div className="relative group">
                  <div className={`absolute inset-0 rounded-full bg-purple-400/20 group-hover:bg-purple-400/30 blur-xl transition-all duration-500 ${dragActive ? 'scale-150' : 'scale-100'}`} />
                  <div className={`relative p-6 rounded-full bg-gradient-to-br from-purple-500 to-indigo-600 transform transition-transform duration-500 ${dragActive ? 'scale-110' : 'group-hover:scale-110 scale-100'}`}>
                    <Upload className="w-10 h-10 text-white" />
                  </div>
                </div>
                <div className="text-center space-y-2">
                  <p className="text-2xl font-medium bg-gradient-to-r from-purple-600 to-indigo-600 bg-clip-text text-transparent">
                    {dragActive ? "Déposez votre fichier ici ✨" : "Glissez-déposez votre CV"}
                  </p>
                  <p className="text-gray-500 text-lg">ou cliquez pour sélectionner un fichier</p>
                </div>
              </>
            )}

            {file && (
              <div className="w-full transform transition-all duration-500">
                <div className="flex items-center justify-between bg-gradient-to-r from-purple-50 to-indigo-50 p-6 rounded-2xl shadow-lg">
                  <div className="flex items-center gap-4">
                    <div className="p-3 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-xl">
                      <FileText className="w-8 h-8 text-white" />
                    </div>
                    <div>
                      <p className="text-lg font-medium text-gray-900">{file.name}</p>
                      <p className="text-gray-500">
                        {(file.size / 1024 / 1024).toFixed(2)} MB
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-6">
                    {uploadStatus === 'uploading' && (
                      <div className="relative">
                        <div className="w-8 h-8 border-4 border-purple-200 border-t-purple-600 rounded-full animate-spin" />
                        <div className="absolute inset-0 rounded-full blur-sm bg-purple-400/30" />
                      </div>
                    )}
                    {uploadStatus === 'success' && (
                      <div className="relative">
                        <div className="absolute inset-0 rounded-full blur-sm bg-green-400/30" />
                        <Check className="w-8 h-8 text-green-500 relative animate-success" />
                      </div>
                    )}
                    {uploadStatus === 'error' && (
                      <div className="relative">
                        <div className="absolute inset-0 rounded-full blur-sm bg-red-400/30" />
                        <AlertCircle className="w-8 h-8 text-red-500 relative animate-error" />
                      </div>
                    )}
                    <button
                      onClick={removeFile}
                      className="p-2 hover:bg-gray-100 rounded-xl transition-colors duration-300"
                      aria-label="Supprimer le fichier"
                    >
                      <X className="w-6 h-6 text-gray-500" />
                    </button>
                  </div>
                </div>

                {uploadStatus === 'success' && (
                  <div className="mt-6 text-center animate-fade-up">
                    <p className="text-xl font-medium text-green-600 mb-2">
                      CV téléchargé avec succès ! 🎉
                    </p>
                    <p className="text-gray-600">
                      Nous allons analyser votre profil et revenir vers vous rapidement
                    </p>
                  </div>
                )}
                
                {uploadStatus === 'error' && (
                  <div className="mt-6 text-center animate-fade-up">
                    <p className="text-xl font-medium text-red-600 mb-2">
                      Oups ! Une erreur est survenue 😥
                    </p>
                    <p className="text-gray-600">
                      Veuillez sélectionner un fichier PDF de moins de 5 MB
                    </p>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Features */}
        <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((feature, i) => (
            <div 
              key={i}
              className="group relative bg-white/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all duration-500 hover:-translate-y-1"
            >
              <div className="absolute inset-0 rounded-2xl bg-gradient-to-r from-purple-400/0 via-purple-400/0 to-purple-400/0 group-hover:from-purple-400/10 group-hover:via-purple-400/5 group-hover:to-purple-400/0 transition-all duration-500" />
              <div className="relative">
                <div className="mb-4 inline-block p-3 bg-purple-100 rounded-xl text-purple-600 group-hover:scale-110 transition-transform duration-500">
                  {feature.icon}
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {feature.title}
                </h3>
                <p className="text-gray-600">
                  {feature.desc}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default CVUpload;