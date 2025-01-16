"use client";
import React from "react";
import { X } from "lucide-react";
import { deleteItem } from "../action/deleteItem";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Modal({ onClose }) {
  const [error, setError] = useState<any>(null);
  const [isDeleting, setIsDeleting] = useState(false);
  const router = useRouter();

  const handleDelete = async () => {
    setIsDeleting(true);
    try {
      const result = await deleteItem("fdfd");
      if (result.success) {
        onClose();
        router.refresh();
      } else {
        throw new Error(result.error || "Failed to delete item");
      }
    } catch (error: any) {
      setError(error.message);
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div>
      <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 transition-all duration-300"></div>
      <div className="fixed w-3/5 h-3/5 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gradient-to-br from-blue-50 to-white p-12 z-50 rounded-xl shadow-2xl border border-blue-100">
        <button className="absolute top-6 right-6 p-2 rounded-full bg-gray-50 hover:bg-gray-100 text-gray-400 hover:text-gray-600 transition-all duration-200">
          <X onClick={onClose} size={20} />
        </button>

        <div className="h-full flex flex-col">
          <h1 className="text-3xl font-semibold text-gray-800 mb-4">
            Modal Title
          </h1>
          <div className="prose prose-gray max-w-none flex-grow">
            <p className="text-gray-600 text-lg leading-relaxed">lala</p>
          </div>

          <div className="absolute bottom-8 right-8 flex gap-4">
            <button className="px-6 py-2.5 bg-green-500 text-white rounded-lg font-medium shadow-lg shadow-green-500/30 hover:shadow-green-500/50 hover:bg-green-600 transition-all duration-200">
              Confirm
            </button>
            <button
              onClick={handleDelete}
              className="px-6 py-2.5 bg-red-500 text-white rounded-lg font-medium shadow-lg shadow-red-500/30 hover:shadow-red-500/50 hover:bg-red-600 transition-all duration-200"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
