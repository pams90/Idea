import { useState, useEffect } from react;
import { Card, CardContent } from @componentsuicard;
import { Button } from @componentsuibutton;
import { Input } from @componentsuiinput;
import { Select, SelectItem } from @componentsuiselect;
import { motion } from framer-motion;

const categories = [
  Productivity, Social Media, Health & Fitness, Finance, 
  Education, Entertainment, AI & Automation, E-commerce
];

export default function IdeaGenerator() {
  const [category, setCategory] = useState();
  const [targetAudience, setTargetAudience] = useState();
  const [problemFocus, setProblemFocus] = useState();
  const [idea, setIdea] = useState(null);
  const [savedIdeas, setSavedIdeas] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() = {
    fetch(httplocalhost5000saved_ideas)
      .then((res) = res.json())
      .then((data) = setSavedIdeas(data.saved_ideas));
  }, []);

  const generateIdea = async () = {
    setLoading(true);
    const response = await fetch(httplocalhost5000generate_idea, {
      method POST,
      headers { Content-Type applicationjson },
      body JSON.stringify({ category, target_audience targetAudience, problem_focus problemFocus })
    });
    const data = await response.json();
    setIdea(data.idea);
    setLoading(false);
  };

  const generateRandomIdea = async () = {
    setLoading(true);
    const response = await fetch(httplocalhost5000generate_idea, {
      method POST,
      headers { Content-Type applicationjson },
      body JSON.stringify({})  Sending empty to trigger random selection
    });
    const data = await response.json();
    setIdea(data.idea);
    setLoading(false);
    saveIdea(Random, data.idea);
  };

  const saveIdea = async (category, idea) = {
    await fetch(httplocalhost5000save_idea, {
      method POST,
      headers { Content-Type applicationjson },
      body JSON.stringify({ category, idea })
    });
    setSavedIdeas([...savedIdeas, { category, idea }]);
  };

  return (
    div className=p-6 max-w-xl mx-auto space-y-4
      h1 className=text-xl font-boldAI App Idea Generatorh1
      Select onValueChange={setCategory} placeholder=Select category
        {categories.map((cat) = (
          SelectItem key={cat} value={cat}{cat}SelectItem
        ))}
      Select
      Input placeholder=Target Audience value={targetAudience} onChange={(e) = setTargetAudience(e.target.value)} 
      Input placeholder=Problem Focus value={problemFocus} onChange={(e) = setProblemFocus(e.target.value)} 
      div className=flex space-x-2
        Button onClick={generateIdea} disabled={loading}{loading  Generating...  Generate Idea}Button
        Button onClick={generateRandomIdea} disabled={loading} variant=secondary{loading  Generating...  Random Idea}Button
      div
      {idea && (
        motion.div initial={{ opacity 0 }} animate={{ opacity 1 }} transition={{ duration 0.5 }}
          Card className=mt-4
            CardContent{idea}CardContent
          Card
        motion.div
      )}
      h2 className=text-lg font-semibold mt-6Saved Ideash2
      div className=space-y-2
        {savedIdeas.map((item, index) = (
          Card key={index}
            CardContent
              strong{item.category}strong {item.idea}
            CardContent
          Card
        ))}
      div
    div
  );
}
