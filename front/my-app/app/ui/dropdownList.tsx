"use client";

import { useState, useRef, useEffect } from "react";

const predefinedTags = [
  "React",
  "Next.js",
  "TypeScript",
  "Tailwind CSS",
  "JavaScript",
  "CSS",
  "HTML",
];

export default function DropdownList() {
  const [inputValue, setInputValue] = useState("");
  const [tags, setTags] = useState<string[]>([]);
  const [filteredTags, setFilteredTags] = useState(predefinedTags);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const dropdownRef = useRef<HTMLUListElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setIsDropdownOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setInputValue(value);
    setFilteredTags(
      predefinedTags.filter((tag) =>
        tag.toLowerCase().includes(value.toLowerCase())
      )
    );
    setIsDropdownOpen(true);
  };

  const addTag = (tag: string) => {
    if (tag && !tags.includes(tag)) {
      setTags([...tags, tag]);
      setInputValue("");
      setFilteredTags(predefinedTags);
      setIsDropdownOpen(false);
      inputRef.current?.focus();
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && inputValue) {
      e.preventDefault();
      addTag(inputValue);
    }
  };

  const removeTag = (tagToRemove: string) => {
    setTags(tags.filter((tag) => tag !== tagToRemove));
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Tag Selector</h1>
      <div className="relative mb-4">
        <input
          ref={inputRef}
          type="text"
          value={inputValue}
          onChange={handleInputChange}
          onKeyDown={handleKeyDown}
          onFocus={() => setIsDropdownOpen(true)}
          placeholder="Type to search or add a tag"
          className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {isDropdownOpen && filteredTags.length > 0 && (
          <ul
            ref={dropdownRef}
            className="absolute z-10 w-full mt-1 bg-white border border-gray-300 rounded-md shadow-lg max-h-60 overflow-auto"
          >
            {filteredTags.map((tag, index) => (
              <li
                key={index}
                onClick={() => addTag(tag)}
                className="px-3 py-2 hover:bg-gray-100 cursor-pointer"
              >
                {tag}
              </li>
            ))}
          </ul>
        )}
      </div>
      <div className="flex flex-wrap gap-2 mb-4">
        {tags.map((tag, index) => (
          <div
            key={index}
            className="bg-blue-100 text-blue-800 px-2 py-1 rounded-md text-sm flex items-center"
          >
            {tag}
            <button
              onClick={() => removeTag(tag)}
              className="ml-2 text-blue-600 hover:text-blue-800 focus:outline-none"
              aria-label={`Remove ${tag} tag`}
            >
              ×
            </button>
          </div>
        ))}
      </div>
      {/* <button
        onClick={() => addTag(inputValue)}
        disabled={!inputValue}
        className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
      >
        Add Tag
      </button> */}
    </div>
  );
}
