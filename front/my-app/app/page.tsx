import Image from "next/image";
import DropdownList from "./ui/dropdownList";
import ListCardsHome from "./ui/listCardsHome";

export default async function Home() {
  return (
    <div className="min-h-screen h-full bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100">
      <DropdownList />
      <ListCardsHome />
    </div>
  );
}
