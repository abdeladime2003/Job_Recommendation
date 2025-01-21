import React, { useState, useEffect } from 'react';
import { Star, Send, Smile, Frown, Meh, Sparkles, Heart, ThumbsUp, MessageCircle , Check} from 'lucide-react';

const FeedbackForm = () => {
  const [rating, setRating] = useState(0);
  const [hoveredRating, setHoveredRating] = useState(0);
  const [comment, setComment] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    // Simuler l'envoi
    await new Promise(resolve => setTimeout(resolve, 1500));
    setSubmitted(true);
    setIsLoading(false);
    
    setTimeout(() => {
      setSubmitted(false);
      setRating(0);
      setComment('');
    }, 3000);
  };

  const getMoodIcon = (rating) => {
    if (rating >= 4) return <Smile className="w-16 h-16 text-emerald-500" />;
    if (rating >= 2) return <Meh className="w-16 h-16 text-yellow-500" />;
    if (rating >= 1) return <Frown className="w-16 h-16 text-red-500" />;
    return null;
  };

  return (
    <div className="min-h-screen py-12 px-4 relative overflow-hidden bg-gradient-to-br from-purple-50 via-indigo-50 to-pink-50">
      {/* Animated background elements */}
      <div className="fixed inset-0 -z-10">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob" />
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-yellow-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000" />
        <div className="absolute bottom-1/4 left-1/3 w-96 h-96 bg-pink-300 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000" />
      </div>

      <div className="max-w-2xl mx-auto">
        {/* Header with floating icons */}
        <div className="relative h-32 mb-8">
          <div className="absolute left-0 top-0 animate-float-slow">
            <MessageCircle className="w-8 h-8 text-purple-400" />
          </div>
          <div className="absolute right-1/4 top-1/4 animate-float-delay">
            <Heart className="w-6 h-6 text-pink-400" />
          </div>
          <div className="absolute right-0 top-0 animate-float">
            <ThumbsUp className="w-8 h-8 text-indigo-400" />
          </div>
          <div className="absolute left-1/4 top-1/3 animate-float-delay-2">
            <Sparkles className="w-6 h-6 text-yellow-400" />
          </div>
        </div>

        <div className="relative group">
          {/* Card glow effect */}
          <div className="absolute -inset-1 bg-gradient-to-r from-purple-600 to-pink-600 rounded-3xl blur-xl opacity-20 group-hover:opacity-30 transition-opacity duration-1000" />
          
          <div className="relative bg-white/80 backdrop-blur-xl rounded-3xl shadow-xl">
            {/* Glass reflection effect */}
            <div className="absolute inset-0 overflow-hidden rounded-3xl">
              <div className="absolute -inset-[500%] animate-glass opacity-20" />
            </div>

            <div className="relative p-8 sm:p-10">
              <h2 className="text-3xl sm:text-4xl font-bold text-center mb-8 bg-gradient-to-r from-purple-600 via-pink-500 to-indigo-600 bg-clip-text text-transparent animate-gradient">
                Partagez votre expérience ✨
              </h2>

              {submitted ? (
                <div className="text-center py-12 space-y-4">
                  <div className="relative">
                    <div className="absolute inset-0 rounded-full blur-md bg-green-200/50" />
                    <div className="relative w-20 h-20 mx-auto bg-gradient-to-br from-green-400 to-emerald-500 rounded-full flex items-center justify-center animate-success">
                      <Check className="w-10 h-10 text-white" />
                    </div>
                  </div>
                  <h3 className="text-2xl font-semibold text-gray-900 mt-6 animate-fade-up">
                    Merci pour votre feedback !
                  </h3>
                  <p className="text-gray-600 animate-fade-up animation-delay-200">
                    Votre avis nous aide à nous améliorer chaque jour.
                  </p>
                </div>
              ) : (
                <form onSubmit={handleSubmit} className="space-y-8">
                  {/* Rating Stars */}
                  <div className="text-center space-y-4">
                    <div className="flex justify-center gap-2">
                      {[1, 2, 3, 4, 5].map((star) => (
                        <button
                          key={star}
                          type="button"
                          className="transform transition-all duration-300 hover:scale-125"
                          onMouseEnter={() => setHoveredRating(star)}
                          onMouseLeave={() => setHoveredRating(0)}
                          onClick={() => setRating(star)}
                        >
                          <div className="relative">
                            <div className="absolute inset-0 blur-md bg-yellow-200/50 scale-150 opacity-0 transition-opacity duration-300 rounded-full" 
                                 style={{ opacity: star <= (hoveredRating || rating) ? 1 : 0 }} />
                            <Star
                              className={`w-12 h-12 transition-all duration-300 ${
                                star <= (hoveredRating || rating)
                                  ? 'text-yellow-400 fill-yellow-400 scale-110 animate-pulse-subtle'
                                  : 'text-gray-300'
                              }`}
                            />
                          </div>
                        </button>
                      ))}
                    </div>
                    {rating > 0 && (
                      <div className="flex justify-center animate-bounce-in">
                        {getMoodIcon(rating)}
                      </div>
                    )}
                  </div>

                  {/* Input Fields */}
                  <div className="space-y-6">
        
                    <div className="space-y-2">
                      <label className="block text-gray-700 font-medium">
                        Votre message
                      </label>
                      <textarea
                        value={comment}
                        onChange={(e) => setComment(e.target.value)}
                        rows={4}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-purple-400 focus:ring-2 focus:ring-purple-200 transition-all duration-300 bg-white/50 hover:bg-white/80"
                        placeholder="Partagez votre expérience avec nous..."
                      />
                    </div>
                  </div>

                  {/* Submit Button */}
                  <button
                    type="submit"
                    disabled={!rating || !comment.trim() || isLoading}
                    className={`group relative w-full py-4 rounded-xl font-medium text-white transition-all duration-500 overflow-hidden
                      ${rating && comment.trim() && !isLoading
                        ? 'bg-gradient-to-r from-purple-600 to-indigo-600 hover:shadow-lg hover:-translate-y-1'
                        : 'bg-gray-300 cursor-not-allowed'
                      }`}
                  >
                    <div className="absolute inset-0 bg-gradient-to-r from-purple-400/0 via-white/20 to-purple-400/0 group-hover:translate-x-full transition-transform duration-1000" />
                    <div className="relative flex items-center justify-center gap-2">
                      {isLoading ? (
                        <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                      ) : (
                        <>
                          <Send className="w-5 h-5" />
                          Envoyer mon feedback
                        </>
                      )}
                    </div>
                  </button>
                </form>
              )}
            </div>
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
        
        @keyframes float {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-20px); }
        }

        @keyframes glass {
          from { transform: translateX(-50%) rotate(0deg); }
          to { transform: translateX(0) rotate(360deg); }
        }

        @keyframes bounce-in {
          0% { transform: scale(0); }
          50% { transform: scale(1.2); }
          100% { transform: scale(1); }
        }

        @keyframes success {
          0% { transform: scale(0) rotate(-180deg); }
          50% { transform: scale(1.2) rotate(20deg); }
          100% { transform: scale(1) rotate(0deg); }
        }

        .animate-blob {
          animation: blob 10s infinite cubic-bezier(0.4, 0, 0.2, 1);
        }

        .animate-float {
          animation: float 3s infinite ease-in-out;
        }

        .animate-float-slow {
          animation: float 4s infinite ease-in-out;
        }

        .animate-float-delay {
          animation: float 3.5s infinite ease-in-out 1s;
        }

        .animate-float-delay-2 {
          animation: float 4.5s infinite ease-in-out 0.5s;
        }

        .animate-glass {
          background: linear-gradient(
            45deg,
            transparent 0%,
            rgba(255, 255, 255, 0.4) 50%,
            transparent 100%
          );
          animation: glass 10s infinite linear;
        }

        .animate-gradient {
          background-size: 300%;
          animation: gradient 10s linear infinite;
        }

        .animation-delay-2000 {
          animation-delay: 2s;
        }

        .animation-delay-4000 {
          animation-delay: 4s;
        }

        @keyframes gradient {
          0% { background-position: 0% 50%; }
          50% { background-position: 100% 50%; }
          100% { background-position: 0% 50%; }
        }

        .animate-pulse-subtle {
          animation: pulse-subtle 2s infinite;
        }

        @keyframes pulse-subtle {
          0% { transform: scale(1); }
          50% { transform: scale(1.05); }
          100% { transform: scale(1); }
        }
      `}</style>
    </div>
  );
};

export default FeedbackForm;