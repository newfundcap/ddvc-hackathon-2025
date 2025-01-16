"use client";
import React from "react";
import { useState } from "react";

import CardHome from "./cardHome";
import Modal from "./modal";

export default function ListCardsHome({ companies }) {
  return (
    <div>
      <div className="m-auto w-[90%] mt-3 mb-20 flex flex-wrap gap-10 justify-center">
        {companies.map((company: any) => (
          <CardHome key={company.id} company={company} />
        ))}
      </div>
    </div>
  );
}
