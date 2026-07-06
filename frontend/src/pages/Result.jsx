import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import Card from '../components/ui/Card';
import Button from '../components/ui/Button';
import { useAuth } from '../context/AuthContext';

const Result = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { user } = useAuth();
  const { results, questions, answers } = location.state || {};

  if (!results) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500">No results found</p>
        <Button onClick={() => navigate('/dashboard')} className="mt-4">
          Go to Dashboard
        </Button>
      </div>
    );
  }

  const { totalQuestions, correct, wrong, skipped } = results;
  const accuracy = totalQuestions > 0 ? Math.round((correct / totalQuestions) * 100) : 0;

  // Get incorrect question IDs for retry
  const incorrectQuestionIds = Object.keys(answers)
    .filter(qId => {
      const q = questions.find(q => q.id === parseInt(qId));
      return q && answers[qId] !== q.correctAnswer;
    })
    .map(id => parseInt(id));

  const stats = [
    { label: 'Score', value: `${correct}/${totalQuestions}`, icon: 'fa-trophy', color: 'text-yellow-500' },
    { label: 'Accuracy', value: `${accuracy}%`, icon: 'fa-bullseye', color: 'text-primary-500' },
    { label: 'Correct', value: correct, icon: 'fa-check-circle', color: 'text-green-500' },
    { label: 'Wrong', value: wrong, icon: 'fa-times-circle', color: 'text-red-500' },
    { label: 'Skipped', value: skipped, icon: 'fa-skip', color: 'text-gray-500' },
  ];

  // Calculate topic-wise performance from the questions
  const topicPerformance = questions.reduce((acc, q) => {
    const topic = q.topic || 'General';
    if (!acc[topic]) {
      acc[topic] = { correct: 0, total: 0 };
    }
    acc[topic].total++;
    if (answers[q.id] === q.correctAnswer) {
      acc[topic].correct++;
    }
    return acc;
  }, {});

  const topicPerformanceArray = Object.entries(topicPerformance).map(([topic, data]) => ({
    topic,
    correct: data.correct,
    total: data.total,
    percentage: Math.round((data.correct / data.total) * 100)
  }));

  // Calculate difficulty-wise performance
  const difficultyPerformance = questions.reduce((acc, q) => {
    const diff = q.difficulty || 'Medium';
    if (!acc[diff]) {
      acc[diff] = { correct: 0, total: 0 };
    }
    acc[diff].total++;
    if (answers[q.id] === q.correctAnswer) {
      acc[diff].correct++;
    }
    return acc;
  }, {});

  const difficultyPerformanceArray = Object.entries(difficultyPerformance).map(([difficulty, data]) => ({
    difficulty,
    correct: data.correct,
    total: data.total,
    percentage: Math.round((data.correct / data.total) * 100)
  }));

  // Identify weak and strong areas
  const weakAreas = topicPerformanceArray
    .filter(t => t.percentage < 50)
    .map(t => t.topic);
  
  const strongAreas = topicPerformanceArray
    .filter(t => t.percentage >= 70)
    .map(t => t.topic);

  // Handle Retry Incorrect
  const handleRetryIncorrect = () => {
    if (incorrectQuestionIds.length === 0) {
      alert('No incorrect questions to retry!');
      return;
    }
    // Filter questions to only incorrect ones
    const retryQuestions = questions.filter(q => incorrectQuestionIds.includes(q.id));
    // Navigate to practice with only incorrect questions
    navigate('/practice', { 
      state: { 
        questions: retryQuestions,
        isRetry: true,
        topicName: 'Incorrect Questions'
      } 
    });
  };

  // Handle Practice Similar
  const handlePracticeSimilar = () => {
    // Get the subject and topic from the first question
    const firstQ = questions[0];
    if (firstQ) {
      navigate(`/practice/${firstQ.topic || 'General'}?subject=${firstQ.subject || ''}&similar=true`);
    } else {
      navigate('/dashboard');
    }
  };

  // Update user stats (in a real app, this would call an API)
  const updateUserStats = () => {
    // This would be an API call in production
    console.log('Updating user stats...', {
      accuracy,
      correct,
      wrong,
      skipped,
      totalQuestions,
      weakAreas,
      strongAreas
    });
  };

  // Call update stats when component loads
  React.useEffect(() => {
    updateUserStats();
  }, []);

  return (
    <div className="max-w-4xl mx-auto space-y-6 animate-fade-in">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900">Practice Results</h1>
        <p className="text-gray-500">Here's how you performed</p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
        {stats.map((stat) => (
          <Card key={stat.label} className="text-center">
            <div className={`text-3xl ${stat.color}`}>
              <i className={`fas ${stat.icon}`} />
            </div>
            <p className="text-2xl font-bold text-gray-900 mt-2">{stat.value}</p>
            <p className="text-sm text-gray-500">{stat.label}</p>
          </Card>
        ))}
      </div>

      {/* Topic-wise Performance */}
      {topicPerformanceArray.length > 0 && (
        <Card>
          <h3 className="text-lg font-semibold text-gray-900 mb-4">📊 Topic-wise Performance</h3>
          <div className="space-y-4">
            {topicPerformanceArray.map((topic) => (
              <div key={topic.topic}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-700">{topic.topic}</span>
                  <span className="font-semibold">{topic.correct}/{topic.total}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2.5">
                  <div
                    className={`h-2.5 rounded-full ${
                      topic.percentage >= 70 ? 'bg-green-500' : 
                      topic.percentage >= 50 ? 'bg-yellow-500' : 'bg-red-500'
                    }`}
                    style={{ width: `${topic.percentage}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Difficulty-wise Performance */}
      {difficultyPerformanceArray.length > 0 && (
        <Card>
          <h3 className="text-lg font-semibold text-gray-900 mb-4">📊 Difficulty-wise Performance</h3>
          <div className="space-y-4">
            {difficultyPerformanceArray.map((diff) => (
              <div key={diff.difficulty}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-700">{diff.difficulty}</span>
                  <span className="font-semibold">{diff.correct}/{diff.total}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2.5">
                  <div
                    className={`h-2.5 rounded-full ${
                      diff.percentage >= 70 ? 'bg-green-500' : 
                      diff.percentage >= 50 ? 'bg-yellow-500' : 'bg-red-500'
                    }`}
                    style={{ width: `${diff.percentage}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </Card>
      )}

      {/* Strong & Weak Areas */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <h3 className="text-lg font-semibold text-green-600 mb-4">💪 Strong Areas</h3>
          {strongAreas.length === 0 ? (
            <p className="text-gray-500 text-sm">No strong areas identified yet</p>
          ) : (
            <div className="space-y-2">
              {strongAreas.map((area) => (
                <div key={area} className="flex items-center gap-2 text-gray-700">
                  <span>✅</span> {area}
                </div>
              ))}
            </div>
          )}
        </Card>

        <Card>
          <h3 className="text-lg font-semibold text-red-600 mb-4">🎯 Areas to Improve</h3>
          {weakAreas.length === 0 ? (
            <p className="text-gray-500 text-sm">No weak areas identified! Great job!</p>
          ) : (
            <div className="space-y-2">
              {weakAreas.map((area) => (
                <div key={area} className="flex items-center gap-2 text-gray-700">
                  <span>📈</span> {area}
                </div>
              ))}
            </div>
          )}
        </Card>
      </div>

      {/* Action Buttons */}
      <div className="flex flex-wrap gap-4">
        <Button onClick={() => navigate('/dashboard')}>
          <i className="fas fa-home mr-2" /> Back to Dashboard
        </Button>
        <Button 
          variant="secondary"
          onClick={handleRetryIncorrect}
          disabled={incorrectQuestionIds.length === 0}
        >
          <i className="fas fa-redo mr-2" /> Retry Incorrect
          {incorrectQuestionIds.length > 0 && (
            <span className="ml-1 text-xs">({incorrectQuestionIds.length})</span>
          )}
        </Button>
        <Button variant="outline" onClick={handlePracticeSimilar}>
          <i className="fas fa-layer-group mr-2" /> Practice Similar
        </Button>
      </div>
    </div>
  );
};

export default Result;