"use client";
import React from "react";
import { X } from "lucide-react";
import { deleteItem } from "../action/deleteItem";
import { useRouter } from "next/navigation";
import { useState } from "react";

import {
  Building2,
  Globe,
  Users,
  Calendar,
  Briefcase,
  FileText,
} from "lucide-react";

export default function Modal({ onClose, company }) {
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

  const cardBgImage = {
    backgroundImage: `url(https://substack-post-media.s3.amazonaws.com/public/images/466308ce-12ae-425f-89ce-acd60f69578e_1279x474.png)`,
  };

  return (
    <div>
      <div className="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 transition-all duration-300"></div>
      <div className="fixed w-3/5 h-4/5 top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-gradient-to-br from-blue-50 to-white p-12 z-50 rounded-xl shadow-2xl border border-blue-100 overflow-y-auto overflow-x-hidden">
        <button className="absolute top-6 right-6 p-2 rounded-full bg-gray-50 hover:bg-gray-100 text-gray-400 hover:text-gray-600 transition-all duration-200">
          <X onClick={onClose} size={20} />
        </button>

        <div className="h-full flex flex-col bg-gradient-to-br from-blue-50 via-white to-purple-50 p-6 rounded-lg">
          <div className="flex items-center space-x-6 mb-8 justify-between">
            <div className="border-b border-gray-200 pb-4 mb-6 ">
              <h1 className="text-3xl font-bold text-gray-900 mb-2">
                {company.name}
              </h1>
              <p className="text-gray-500 text-sm">{company.website}</p>
            </div>
            <div className="w-40 h-40">
              <img src={company.logo_url} alt="" whidth="10" height="10"/>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div className="flex items-center space-x-3">
              <div>
                <p className="text-sm font-medium text-gray-500">Country</p>
                <p className="text-gray-900">{company.country}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3">
              <Briefcase className="w-5 h-5 text-blue-500"/>
              <div>
                <p className="text-sm font-medium text-gray-500">Sector</p>
                <p className="text-gray-900">{company.sector}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3">
              <div>
                <p className="text-sm font-medium text-gray-500">
                  Funding Stage
                </p>
                <p className="text-gray-900">{company.funding_stage}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3">
              <Calendar className="w-5 h-5 text-blue-500"/>
              <div>
                <p className="text-sm font-medium text-gray-500">Founded</p>
                <p className="text-gray-900">{company.creation_date}</p>
              </div>
            </div>

            <div className="flex items-center space-x-3">
              <Users className="w-5 h-5 text-blue-500"/>
              <div>
                <p className="text-sm font-medium text-gray-500">
                  Full-time Employees
                </p>
                <p className="text-gray-900">{company.full_time_employees}</p>
              </div>
            </div>
          </div>

          <div className="flex-grow">
            <div className="flex items-center space-x-3 mb-3">
              <FileText className="w-5 h-5 text-blue-500"/>
              <h2 className="text-lg font-semibold text-gray-900">
                Description
              </h2>
            </div>
            <p className="text-gray-700 leading-relaxed">
              {company.description}
            </p>
          </div>
          <div>
            <h2 className="text-lg font-semibold text-gray-900 mb-3">Scores</h2>
            <p className="text-gray-700">
              <ul>
                {company.rankers.map((elem, index) => {
                  return <li key={elem.name}>{elem.name}: {elem.score}</li>;
                })}
              </ul>
            </p>
          </div>
          <div>
            <h2 className="text-lg font-semibold text-gray-900 mb-3">Warnings</h2>
            <p className="text-gray-700">
              <ul>
                {company.filters.map((elem, index) => {
                  return <li key={elem.name}>{elem.name}</li>;
                })}
              </ul>
            </p>
          </div>
          <div>
            <h2 className="text-lg font-semibold text-gray-900 mb-3">Team</h2>
            <p className="text-gray-700">
              <ul>
                {company.team.map((elem, index) => {
                  return <li key={index}>{elem.first_name} {elem.last_name}</li>;
                })}
              </ul>
            </p>
          </div>
        </div>

        <div className="absolute bottom-8 right-8 flex gap-4">
          <button
              className="px-6 py-2.5 bg-green-500 text-white rounded-lg font-medium shadow-lg shadow-green-500/30 hover:shadow-green-500/50 hover:bg-green-600 transition-all duration-200">
            Approve
          </button>
          <button
              onClick={handleDelete}
            className="px-6 py-2.5 bg-red-500 text-white rounded-lg font-medium shadow-lg shadow-red-500/30 hover:shadow-red-500/50 hover:bg-red-600 transition-all duration-200"
          >
            Decline
          </button>
        </div>
      </div>
    </div>
  );
}
