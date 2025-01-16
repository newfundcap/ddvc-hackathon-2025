import Image from "next/image";
import DropdownList from "./ui/dropdownList";
import ListCardsHome from "./ui/listCardsHome";
import ButtonToAddCompany from "./ui/buttonToAddCompany";

export default async function Home() {
  // const dataCompanies =  await fetch("https://api.example.com/data");
  // make a fetch that fetches the data from the api
  // then pass the data to the ListCardsHome component

  // i want fake values for the cards

  const fakeCompanies = [
    {
      id: 1,
      name: "TechNova",
      country: "USA",
      sector: "Technology",
      contact: "contact@technova.com",
      funding_stage: "Series A",
      creation_date: "2015-06-15",
      investors: JSON.stringify(["VC Fund A", "Angel Investor B"]),
      revenue: 12000000.5,
      revenue_growth: 0.15,
      total_amount_raised: 25000000,
      description:
        "TechNova is a leader in AI-driven solutions for the tech industry.",
      website: "https://www.technova.com",
      linkedin: "https://www.linkedin.com/company/technova",
      harmonic_id: "HN12345",
      pdl_id: "PDL67890",
      full_time_employees: 150,
      full_time_employees_growth: 0.2,
      created_at: "2025-01-01T12:00:00",
      updated_at: "2025-01-15T10:30:00",
    },
    {
      id: 2,
      name: "GreenFuture",
      country: "Germany",
      sector: "Renewable Energy",
      contact: "info@greenfuture.de",
      funding_stage: "Series B",
      creation_date: "2018-03-20",
      investors: JSON.stringify(["Green Energy Ventures", "EcoFund"]),
      revenue: 8000000.75,
      revenue_growth: 0.25,
      total_amount_raised: 18000000,
      description:
        "GreenFuture specializes in sustainable energy solutions for a cleaner planet. fjfbjefbj egkjjtkjektj jerktjektjk tjektjektjke jetjtejte jtekt lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      website: "https://www.greenfuture.de",
      linkedin: "https://www.linkedin.com/company/greenfuture",
      harmonic_id: "HN67890",
      pdl_id: "PDL12345",
      full_time_employees: 200,
      full_time_employees_growth: 0.3,
      created_at: "2025-01-01T12:00:00",
      updated_at: "2025-01-15T10:30:00",
    },
    {
      id: 3,
      name: "EduSmart",
      country: "India", // add
      sector: "Education Technology", // add
      contact: "support@edusmart.in",
      funding_stage: "Seed", // add
      creation_date: "2020-11-01", //add
      investors: JSON.stringify(["EdTech Angels", "StartUp Incubator"]),
      revenue: 3000000.0,
      revenue_growth: 0.4,
      total_amount_raised: 5000000,
      description:
        "EduSmart offers innovative solutions for online learning and skill development.",
      website: "https://www.edusmart.in", // add
      linkedin: "https://www.linkedin.com/company/edusmart", // add
      harmonic_id: "HN54321",
      pdl_id: "PDL98765",
      full_time_employees: 50, // add
      full_time_employees_growth: 0.5,
      created_at: "2025-01-01T12:00:00",
      updated_at: "2025-01-15T10:30:00",
    },
  ];

  return (
    <div className="min-h-screen h-full">
      <ButtonToAddCompany />
      <DropdownList />
      <ListCardsHome companies={fakeCompanies} />
    </div>
  );
}
