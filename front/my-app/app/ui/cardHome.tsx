"use client";

import Link from "next/link";
import Image from "next/image";
import { useEffect, useRef, useState } from "react";
import { number } from "zod";

import Modal from "./modal";

export default function CardHome({ company }) {
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });
  const [mousePosition, setMousePosition] = useState({ mouseX: 0, mouseY: 0 });
  const [mouseLeaveDelay, setMouseLeaveDelay] = useState(null);
  const cardRef = useRef<HTMLDivElement>(null);
  const [showModal, setShowModal] = useState<boolean>(false);

  const handleShowModal = () => {
    setShowModal(!showModal);
  };

  useEffect(() => {
    if (cardRef.current) {
      setDimensions({
        width: cardRef.current.offsetWidth,
        height: cardRef.current.offsetHeight,
      });
    }
  }, []);

  const mousePX = mousePosition.mouseX / dimensions.width;
  const mousePY = mousePosition.mouseY / dimensions.height;

  const homeCardStyle = {
    transform: `rotateY(${mousePX * 30}deg) rotateX(${mousePY * -30}deg)`,
  };
  const cardBgTransform = () => {
    return {
      transform: `translateX(${mousePX * -40}px) translateY(${
        mousePY * -40
      }px)`,
    };
  };

  const cardBgImage = { backgroundImage: `url('/lala.webp')` };

  const handleMouseMove = (e: any) => {
    if (cardRef.current) {
      const rect = cardRef.current.getBoundingClientRect();

      const scrollTop = window.scrollY || window.pageYOffset;
      const elementTop = rect.top + scrollTop;
      setMousePosition({
        mouseX: e.pageX - rect.left - dimensions.width / 2,
        mouseY: e.pageY - elementTop - dimensions.height / 2,
      });
    }
  };

  const handleMouseEnter = () => {
    if (mouseLeaveDelay) {
      clearTimeout(mouseLeaveDelay);
      setMouseLeaveDelay(null);
    }
  };

  const handleMouseLeave = () => {
    setTimeout(() => {
      setMousePosition({ mouseX: 0, mouseY: 0 });
    }, 1000);
  };

  return (
    <div>
      {showModal ? (
        <Modal onClose={handleShowModal} company={company} />
      ) : (
        <></>
      )}
      <span onClick={handleShowModal}>
        <div
          className=" m-2.5 perspective-800 transform-style-3d text-slate-200 cursor-pointer
    hover:home-card-info-translateY hover:home-card-info-opacity
    hover:card-home-info-after hover:home-card-bg hover:home-card"
          ref={cardRef}
          onMouseMove={handleMouseMove}
          onMouseEnter={handleMouseEnter}
          onMouseLeave={handleMouseLeave}
        >
          {/*home-card-wrap */}

          <div
            className="home-card relative flex-grow-0 flex-shrink-0 w-60
       bg-[#333] overflow-hidden h-80 rounded-[10px]"
            style={homeCardStyle}
          >
            {/*"home-card"  :style="cardStyle"*/}
            <div
              className="home-card-bg opacity-50 absolute -top-5 -left-5 
        h-full p-5 bg-no-repeat bg-center bg-cover pointer-events-none"
              style={{ ...cardBgTransform(), ...cardBgImage }}
            ></div>
            {/*class="home-card-bg" :style="[cardBgTransform, cardBgImage]"*/}
            <div
              className="home-card-info p-5 absolute bottom-0 text-white
        after:content-[''] after:absolute after:top-0 after:left-0 after:z-0 after:w-full 
        after:h-full after:bg-blend-overlay after:opacity-0 after:translate-y-full"
            >
              {/*class="home-card-info"*/}
              <h1 className="leading-6 mb-2.5 relative z-[1] text-3xl font-bold font-playfair_display">
                {company.name}
              </h1>
              <p className="mt-2.5 opacity-0 relative z-[1] font-medium text-lg">
                {company.description}
              </p>
            </div>
          </div>
        </div>
      </span>
    </div>
  );
}
