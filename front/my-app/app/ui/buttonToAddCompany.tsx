"use client";
import React from "react";
import { useState } from "react";
import ModalToAddCompany from "./modalToAddCompany";

export default function ButtonToAddCompany() {
  const [showModal, setShowModal] = useState<boolean>(false);

  const handleShowModal = () => {
    setShowModal(!showModal);
  };

  return (
    <div>
      {showModal ? <ModalToAddCompany onClose={handleShowModal} /> : <></>}
      <div onClick={handleShowModal} className="fixed top-10 left-10">
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ">
          Add Company
        </button>
      </div>
    </div>
  );
}
