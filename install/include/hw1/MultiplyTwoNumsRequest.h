// Generated by gencpp from file hw1/MultiplyTwoNumsRequest.msg
// DO NOT EDIT!


#ifndef HW1_MESSAGE_MULTIPLYTWONUMSREQUEST_H
#define HW1_MESSAGE_MULTIPLYTWONUMSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace hw1
{
template <class ContainerAllocator>
struct MultiplyTwoNumsRequest_
{
  typedef MultiplyTwoNumsRequest_<ContainerAllocator> Type;

  MultiplyTwoNumsRequest_()
    : a(0.0)
    , b(0.0)  {
    }
  MultiplyTwoNumsRequest_(const ContainerAllocator& _alloc)
    : a(0.0)
    , b(0.0)  {
  (void)_alloc;
    }



   typedef double _a_type;
  _a_type a;

   typedef double _b_type;
  _b_type b;





  typedef boost::shared_ptr< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct MultiplyTwoNumsRequest_

typedef ::hw1::MultiplyTwoNumsRequest_<std::allocator<void> > MultiplyTwoNumsRequest;

typedef boost::shared_ptr< ::hw1::MultiplyTwoNumsRequest > MultiplyTwoNumsRequestPtr;
typedef boost::shared_ptr< ::hw1::MultiplyTwoNumsRequest const> MultiplyTwoNumsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator1> & lhs, const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator2> & rhs)
{
  return lhs.a == rhs.a &&
    lhs.b == rhs.b;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator1> & lhs, const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hw1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6f4f9f1b571de73ae8592a1438fd23f3";
  }

  static const char* value(const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6f4f9f1b571de73aULL;
  static const uint64_t static_value2 = 0xe8592a1438fd23f3ULL;
};

template<class ContainerAllocator>
struct DataType< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hw1/MultiplyTwoNumsRequest";
  }

  static const char* value(const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 a\n"
"float64 b\n"
"\n"
;
  }

  static const char* value(const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MultiplyTwoNumsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hw1::MultiplyTwoNumsRequest_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<double>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<double>::stream(s, indent + "  ", v.b);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HW1_MESSAGE_MULTIPLYTWONUMSREQUEST_H
