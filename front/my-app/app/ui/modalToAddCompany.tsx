"use client";
import React from "react";
import { X } from "lucide-react";

import { useState } from "react";
import FormToAddCompany from "./formToAddCompany";

export default function ModalToAddCompany({ onClose }) {
  return (
    <div>
      <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 transition-all duration-300"></div>
      <div className="fixed w-3/5 h-3/5 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gradient-to-br from-blue-50 to-white p-12 z-50 rounded-xl shadow-2xl border border-blue-100">
        <button className="absolute top-6 right-6 p-2 rounded-full bg-gray-50 hover:bg-gray-100 text-gray-400 hover:text-gray-600 transition-all duration-200">
          <X onClick={onClose} size={20} />
        </button>
        <FormToAddCompany />
      </div>
    </div>
  );
}
