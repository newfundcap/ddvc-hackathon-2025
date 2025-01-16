import Image from "next/image";
import DropdownList from "./ui/dropdownList";
import ListCardsHome from "./ui/listCardsHome";
import ButtonToAddCompany from "./ui/buttonToAddCompany";

export default async function Home() {
  // const dataFromBack =  await fetch("https://api.example.com/data");
  // make a fetch that fetches the data from the api
  // then pass the data to the ListCardsHome component

  return (
    <div className="min-h-screen h-full bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100">
      <ButtonToAddCompany />
      <DropdownList />
      <ListCardsHome />
    </div>
  );
}
