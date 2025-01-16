"use client";
import React from "react";
import { X } from "lucide-react";
import DropdownList from "./dropdownList";
import ListCardsHome from "./listCardsHome";

import { useState } from "react";

export default function FilterDropdownToCompany({ companies, rankers }) {
  return (
    <div>
      <DropdownList rankers={rankers} />
      <ListCardsHome companies={companies} />
    </div>
  );
}
