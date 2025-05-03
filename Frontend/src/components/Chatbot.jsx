import React, { useState } from 'react';
import SouthEastOutlinedIcon from '@mui/icons-material/SouthEastOutlined';
import { motion } from 'framer-motion';
import SmartToyOutlinedIcon from '@mui/icons-material/SmartToyOutlined';
import SendOutlinedIcon from '@mui/icons-material/SendOutlined';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import { useEffect, useRef } from 'react';


const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const chatEndRef = useRef(null);


  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hi! How can I help you today?' },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:8000/api/chatbot', { message: input });
      const botMessage = {
        sender: 'bot',
        text: res.data.message || 'Sorry, I didn’t get that.',
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      setMessages(prev => [
        ...prev,
        { sender: 'bot', text: 'Error connecting to server.' },
      ]);
      console.log("Error:",err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div className="fixed bottom-6 right-6 z-50">
      <motion.div
        animate={{ width: isOpen ? 480 : 64, height: isOpen ? 600 : 64 }}
        className="bg-gray-50 border-2 border-solid border-[#5c47e0] shadow-2xl rounded-2xl overflow-hidden transition-all duration-300 flex flex-col"
      >
        {isOpen ? (
          <>
            <div className="flex items-center justify-between p-3 text-[#5c47e0] border-b-2 border-dashed">
              <button
                onClick={() => setIsOpen(false)}
                className="hover:opacity-75"
              >
                <SouthEastOutlinedIcon />
              </button>
              <h2 className="text-lg font-semibold">Chatbot</h2>
              <div className="w-6" />
            </div>

            <div className="flex-1 p-4 overflow-y-auto text-sm">
              {messages.map((msg, idx) => (
                <div
                  key={idx}
                  className={`relative px-4 py-2 my-1 rounded-lg break-words max-w-[80%] w-fit ${
                    msg.sender === 'user'
                      ? 'ml-auto bg-blue-100 text-right rounded-tr-none'
                      : 'mr-auto bg-gray-200 text-left rounded-tl-none'
                  }`}
                >
                  {/* Arrow */}
                  <span
                    className={`absolute top-0 w-0 h-0 border-solid border-[10px] ${
                      msg.sender === 'user'
                        ? 'right-0 border-t-transparent border-b-blue-100 border-l-transparent border-r-transparent -translate-y-1/2'
                        : 'left-0 border-t-transparent border-b-gray-200 border-l-transparent border-r-transparent -translate-y-1/2'
                    }`}
                  ></span>

                  <ReactMarkdown>{msg.text}</ReactMarkdown>
                </div>
              ))}


              {loading && (
                <div className="text-xs text-gray-500 italic mt-2">Bot is typing...</div>
              )}
                <div ref={chatEndRef}/>
            </div >

            <div className="p-2 flex">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
                className="w-full px-3 py-2 border-2 rounded-md text-sm focus:outline-none border-[#5c47e0]"
                placeholder="Type a message..."
              />
              <div className="pl-1">
                <button
                  onClick={sendMessage}
                  className="justify-center align-end p-1 pt-1 h-10 border-2 border-[#5c47e0] rounded-md hover:bg-gray-200"
                >
                  <SendOutlinedIcon style={{ color: '#5c47e0' }} />
                </button>
              </div>
            </div>
          </>
        ) : (
          <button
            onClick={() => setIsOpen(true)}
            className="w-full h-full flex items-center justify-center border-solid text-[#5c47e0] rounded-2xl hover:bg-gray-200 duration-150 ease-in-out hover:scale-125"
          >
            <SmartToyOutlinedIcon fontSize="large" style={{ color: '#5c47e0' }} />
          </button>
        )}
      </motion.div>
    </div>
  );
};

export default Chatbot;
